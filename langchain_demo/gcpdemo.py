from typing import Optional
import os
from google.api_core.client_options import ClientOptions
from google.cloud import documentai  # type: ignore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/HP/Downloads/gcp-key2.json"

project_id = "472752587196"
location = "us"
processor_id = "c2f0274a752e9c44"
file_path = "C:/Users/HP/Downloads/testreceipt.pdf"
mime_type = "application/pdf"
#entities = ["tan1","name"]
def process_document_sample(
    project_id: str,
    location: str,
    processor_id: str,
    file_path: str,
    mime_type: str,
    field_mask: Optional[str] = None,
    processor_version_id: Optional[str] = None,
    entities: Optional[list] = None  # Adding entity_types as an optional parameter
) -> None:
    # You must set the `api_endpoint` if you use a location other than "us".
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")

    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    if processor_version_id:
        # The full resource name of the processor version, e.g.:
        # `projects/{project_id}/locations/{location}/processors/{processor_id}/processorVersions/{processor_version_id}`
        name = client.processor_version_path(
            project_id, location, processor_id, processor_version_id
        )
    else:
        # The full resource name of the processor, e.g.:
        # `projects/{project_id}/locations/{location}/processors/{processor_id}`
        name = client.processor_path(project_id, location, processor_id)

    # Read the file into memory
    with open(file_path, "rb") as image:
        image_content = image.read()

    # Load binary data
    raw_document = documentai.RawDocument(content=image_content, mime_type=mime_type)

    # If entity_types are provided, include them in the request
    if entities:
        # Specify entity types in the request
        request = documentai.ProcessRequest(
            name=name,
            raw_document=raw_document,
            field_mask=field_mask,
            entities=entities  # Set the entity_types
        )
    else:
        # If no entity types are passed, default to regular processing
        request = documentai.ProcessRequest(
            name=name,
            raw_document=raw_document,
            field_mask=field_mask,
        )

    # Process the document
    result = client.process_document(request=request)

    # For a full list of `Document` object attributes, reference this page:
    # https://cloud.google.com/document-ai/docs/reference/rest/v1/Document
    document = result.document

    # Read the text recognition output from the processor
    print("The document contains the following text:")
    print(document.text)

    # Optional: Print recognized entities (if any)
    if document.entities:
        print("Recognized entities:")
        for entity in document.entities:
            print(f"Entity: {entity.type_}, Value: {entity.mention_text}")


# [END documentai_process_document_processor_version]
# [END documentai_process_document]
# Call with some example entity types (if known)
process_document_sample(
  project_id="472752587196",
  location="us",
  processor_id="c2f0274a752e9c44",
  file_path="C:/Users/HP/Downloads/testreceipt.pdf",
  mime_type="application/pdf",
  #entities=["tan", "name"]  # Example of entity types you want to extract
)
