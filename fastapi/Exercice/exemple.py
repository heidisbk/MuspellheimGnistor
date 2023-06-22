from typing import Literal, List, Union
from pydantic import BaseModel
from fastapi import FastAPI, File, UploadFile
import uvicorn


app = FastAPI()

class BlogArticles(BaseModel):
    title: str
    content: str
    author: str = "Anonymous Author"
    avg_reading_time: Union[int, float]
    category: Literal["Tech", "Environment", "Politics"] = "Tech"
    tags: List[str] = None 


@app.post("/another-post-endpoint")
async def another_post_endpoint(blog_article: BlogArticles):
    example_data = {
        'title': blog_article.title,
        'content': blog_article.content,
        'author': blog_article.author,
        'average_reading_time': blog_article.avg_reading_time, 
        'category': blog_article.category,
        'tags': blog_article.tags # Accepts only a list of strings, and default is None (meaning nothing)
    }
    return example_data


@app.post("/post-picture", tags=["Blog Endpoints"])
async def post_picture(file: UploadFile= File(...)):
    """
    Upload a picture and read its file name.
    """
    return {"picture": file.filename}


if "__main__" == __name__:
    uvicorn.run(app, host="0.0.0.0", port=8000)