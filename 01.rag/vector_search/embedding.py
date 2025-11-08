
from google import genai

import time

"""
 Google Text Embedding models
* Manual web site : https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings/get-text-embeddings#google-models
* Related to task types: https://github.com/GoogleCloudPlatform/generative-ai/blob/main/embeddings/task-type-embedding.ipynb

"""

#-- Generate embedding using text-multilingual --

def gemini_embedding_func(client:genai.Client, 
                          model:str, 
                          contents,
                          task_type:str="SEMANTIC_SIMILARITY",    
                          output_dimensionality:int=768,
                          ):

        from google.genai.types import EmbedContentConfig

        start_time = time.perf_counter_ns()

        # https://googleapis.github.io/python-genai/genai.html#genai.types.EmbedContentConfig
        embed_config = EmbedContentConfig(
                auto_truncate=True,
                # task types ref : https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api#parameter-list
                task_type=task_type,  
                mime_type="text/plain",
                output_dimensionality=output_dimensionality,  
                # title="title of the text" # when task type is RETRIEVAL_DOCUMENT
        )

        result = client.models.embed_content(
                model=model,
                contents=contents,
                config=embed_config
        )

        end_time = time.perf_counter_ns()

        latency = (end_time - start_time)
        print(f"Latency (ns): {latency*1e-6:.2f} ms")

        return result.embeddings[0].values


# Function to find similar texts in a DataFrame based on cosine similarity --

def find_similar_texts(client:genai.Client, 
                       model, 
                       query_text,
                       df, 
                       embedding_column='feature_vector', 
                       text_column='text', 
                       top_k=5):
        
        from scipy.spatial.distance import cosine


        # Generate embedding for query text
        query_embedding = gemini_embedding_func(
                client=client,
                model=model,
                task_type="SEMANTIC_SIMILARITY",
                output_dimensionality=3072,
                contents=query_text
        )

        # Calculate similarities
        similarities = []
        for idx, row in df.iterrows():
                similarity = 1 - cosine(query_embedding, row[embedding_column])
                similarities.append({'text': row[text_column], 'similarity': similarity})

        # Sort by similarity and get top k results
        results = sorted(similarities, key=lambda x: x['similarity'], reverse=True)[:top_k]

        return results