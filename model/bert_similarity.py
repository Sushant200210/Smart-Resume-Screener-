from sentence_transformers import SentenceTransformer, util
import tokenizer

model = SentenceTransformer('all-MiniLM-L6-v2')  



def get_similarity(resume_text: str, jd_text: str) -> float:
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    jd_embedding = model.encode(jd_text, convert_to_tensor=True)
    similarity_score = util.pytorch_cos_sim(resume_embedding, jd_embedding)
    return float(similarity_score)



if __name__ == "__main__":
    jd = "Looking for a Python developer with experience in machine learning and NLP."
    resume = "Experienced in Python, scikit-learn, deep learning, and natural language processing."
    score = get_similarity(resume, jd)
    print(f"Similarity score: {score:.2f}")


