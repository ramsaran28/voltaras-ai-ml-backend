from google.cloud import storage
import os

BUCKET_NAME = "voltaras-artifacts"


def upload_file(local_path: str, destination_path: str):
    """
    Uploads a file to GCS.
    If upload fails, raises exception (handled upstream).
    """

    if not os.path.exists(local_path):
        raise FileNotFoundError(f"{local_path} does not exist")

    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)

    if not bucket.exists():
        raise RuntimeError(f"GCS bucket {BUCKET_NAME} does not exist")

    blob = bucket.blob(destination_path)
    blob.upload_from_filename(local_path)
    blob.make_public()

    return blob.public_url
