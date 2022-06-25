import pytest
from sqlalchemy import true
from app import schemas


@pytest.mark.parametrize("title, content, published",
[
    ("my first post", "my first content", True)
])
def test_create_some_posts(authorized_client, test_user, title, content, published):
    res = authorized_client.post("/posts/", 
                                json={"title":title, "content":content, "published": published})
    created_posts = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_posts.title == title
    assert created_posts.content == content
    assert created_posts.published == published
    assert created_posts.owner_id == test_user['id']

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts/")
    print(res.json())
    assert res.status_code == 200


@pytest.mark.parametrize("title, content",
[
    ("my default post ", "my default content")
])
def test_create_post_default_published_true(authorized_client, test_user, title, content):
    res = authorized_client.post("/posts/", 
                                json={"title":title, "content":content})
    created_posts = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_posts.title == title
    assert created_posts.content == content
    assert created_posts.published == True
    assert created_posts.owner_id == test_user['id']

def test_unauthorized_user_create_post(client):
    res = client.post("/posts/", 
                                json={"title":"titolo", "content":"contenuto"})
    assert res.status_code == 401

def test_unauthorized_user_delete_post(client, test_user):
    res = client.delete(f"/posts/{1}")
    assert res.status_code == 401

def test_delete_other_user_post(authorized_client, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[3].id}")
    assert res.status_code == 403

def test_update_post(authorized_client, test_user, test_posts):
    data = {
        "title":"titolo aggiornato",
        "content":"contenuto aggiornato",
        "id" : test_posts[0].id 
    }
    
    res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
    updated_post = schemas.Post(**res.json())
    assert res.status_code == 200
    assert updated_post.title == data['title']
    assert updated_post.content == data['content']