from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def load_cv(cv_file_path: str) -> Document:
    """
    Retrieves pdf file from the provided path and extracts the text into an instance of class Document
    from langchain_core.document module.
    :param cv_file_path: full path to the file in pdf format
    :return: instance of class Document from langchain_core.document module
    """
    loader = PyPDFLoader(cv_file_path)
    cv = loader.load()
    return cv