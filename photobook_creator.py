from PIL import Image
import logging

from payload import PAYLOAD
import os

from models.photobook_models import (
    SingleSquare,
    TwoVertical,
    TwoHorizontal,
    FourSquares,
    OneVerticalOneSquare,
    SingleHorizontal,
)


SIZE = {"width": 755, "height": 755}  # 20 x 20 cm
FINAL_PDF_PATH = (
    "photos/final_photobook.pdf"  # where to store the final PDF containing all pages
)


MODEL_MAPPER = {
    0: SingleSquare,
    1: TwoVertical,
    2: TwoHorizontal,
    3: FourSquares,
    4: OneVerticalOneSquare,
    5: SingleHorizontal,
}


def photobook_creator(payload):
    """Function responsible for creating the photobook according to the layout provided by the
    input payload.

    Args:
        payload (dict): The input payload defining the page & photo information. For each page,
        the photos are defined in terms of position on the page.

    Returns:
        Boolean: True/False according to success.
    """
    try:
        if not payload:
            logging.error(f"No payload provided for photobook creator.")
            return False
        final_images = []
        photobook_width = SIZE.get("width")
        photobook_height = SIZE.get("height")

        image_payload_data = __normalize_payload(payload.get("page_data"))

        page_counter = 1
        for page, page_data in image_payload_data.items():
            background_color = page_data[0].get("background_color")
            page_img = Image.new(
                "RGB",
                (int(photobook_width), int(photobook_height)),
                color=background_color,
            )

            for image_data in page_data:
                position = image_data.get("position")
                mode = image_data.get("mode")
                image_uri = image_data.get("image_uri")
                if not image_uri:
                    return False
                image = _open_image(image_uri)
                if not image:
                    return False
                model = _get_model(mode, position, photobook_width, photobook_height)
                if not model:
                    return False
                image = image.resize((model.image_width, model.image_height))

                page_img.paste(image, model.position)
                image.close()
            final_images.append(page_img)
            page_counter += 1
        # save all page images to a pdf file
        final_images[0].save(
            FINAL_PDF_PATH,
            "PDF",
            resolution=100.0,
            save_all=True,
            append_images=final_images[1:],
        )
        return True
    except Exception as e:
        logging.error(f"Could not create photobook. Exception: {e}")
        return False


def _get_model(mode, position, photobook_width, photobook_height):
    """Helper function to retrieve the model for the specific layout mode.

    Args:
        mode (int): The layout mode.
        position (str): The position of the specific image.
    """
    model = MODEL_MAPPER.get(mode)
    if not model:
        logging.error(f"No model found for mode: {mode}")
        return None
    model_instance = model(position, photobook_width, photobook_height)
    return model_instance


def __normalize_payload(payload):
    """Helper Function to normalize the payload data to a format that is grouped per page.

    Args:
        payload (list): The image & page data.

    Return:
        dict: The payload data in the format per page.
    """
    final_dict = {}

    for item in payload:
        page = item.get("page")
        if page not in final_dict.keys():
            final_dict[page] = []
        temp_dict = {
            "background_color": item.get("colorTheme", "#FFFFFF"),
            "mode": item.get("mode"),
            "position": item.get("position"),
            "image_uri": item.get("image", {}).get("uri"),
        }
        final_dict[page].append(temp_dict)
    return final_dict


def _open_image(image_uri):
    """Helper Function to retrieve the photo object from the S3 server and return an Image instance.

    Args:
        image_uri (str): The URI of the photo on the s3 server.

    Returns:
        Image(object): Image object, None on failure.
    """
    try:
        img = Image.open(os.path.normpath(image_uri))
        return img
    except Exception as e:
        logging.error(f"Could not open image with URI: {image_uri}. Exception: {e}")
        return None


if __name__ == "__main__":
    photobook_creator(PAYLOAD)
