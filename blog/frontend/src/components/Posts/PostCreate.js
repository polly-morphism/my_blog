import React, {useState} from "react";
import ReactDOM from "react-dom";
import axios, { post } from 'axios';


const PostCreate = ({match}) => {
    const[title, setTitle]=useState("")
    const[postText, setPostText]=useState("")
    const[img, setImg]=useState(undefined)
    const handleCreatePost = (e) => {
    e.preventDefault();
    let form_data = new FormData();
    form_data.append('photo', img, img.name);
    form_data.append('title', title);
    form_data.append('content', postText);
    let url = 'http://127.0.0.1:8000/blogposts/';
    axios.post(url, form_data, {
      headers: {
        'content-type': 'multipart/form-data'
      }
    })
        .then(res => {
          console.log(res.data);
        })
        .catch(err => console.log(err))
  };
    return (
    <div className="create-post">
        <div className="create-post-title">
            <div className="create-post-text">
            Create Post
            </div>
            <input value={title} onChange={event => setTitle(event.target.value)} type="text" placeholder="Title"/>
        </div>
        <textarea onChange={event => setPostText(event.target.value)} name="Text" placeholder="Text">{postText}</textarea>
        <input onChange={event => {console.log(event.target.files[0]);
            setImg(event.target.files[0])}} type="file" name="file"/>
        <button className="button-scroll" onClick={handleCreatePost}>Post</button>
    </div>
)};

export default PostCreate
