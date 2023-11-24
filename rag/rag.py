from fastapi import APIRouter
from txtai.api import application, Extension


class RAG(Extension):
    """
    API extension
    """

    def __call__(self, app):
        app.include_router(RAGRouter().router)


class RAGRouter:
    """
    API router
    """

    router = APIRouter()

    @staticmethod
    @router.get("/rag")
    def rag(text: str):
        """
        Runs a retrieval augmented generation (RAG) pipeline.

        Args:
            text: input text

        Returns:
            response
        """

        # Run embeddings search
        results = application.get().search(text, 3)
        context = " ".join([x["text"] for x in results])

        prompt = f"""
        Answer the following question using only the context below.

        Question: {text}
        Context: {context}
        """

        return {
            "response": application.get().pipeline("llm", (prompt,))
        }