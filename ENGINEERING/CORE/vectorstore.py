#from langchain_community.vectorstores import FAISS

#from core.embeddings import get_embeddings


#def create_vector_store(chunks):

#    embeddings = get_embeddings()

#    db = FAISS.from_texts(
#        chunks,
#        embedding=embeddings
#    )

#    db.save_local("faiss_index")

#    return db
###############################################

from langchain_community.vectorstores import FAISS

from core.embeddings import get_embeddings


class VectorStore:

    INDEX_PATH = "data/faiss_index"

    @classmethod
    def create(cls, chunks):

        embeddings = get_embeddings()

        db = FAISS.from_texts(chunks, embeddings)

        db.save_local(cls.INDEX_PATH)

        return db

    @classmethod
    def load(cls):

        embeddings = get_embeddings()

        return FAISS.load_local(
            cls.INDEX_PATH,
            embeddings,
            allow_dangerous_deserialization=True,
        )
