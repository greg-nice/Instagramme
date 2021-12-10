import React, { useEffect, useState } from "react";
// import { useSelector } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import "./DisplayPost.css";

import { deletePost, editPost } from "../../store/posts";

import Comment from "../Comments/CommentForm";

function DisplayPost({ postId, setShowModal }) {
  const sessionUser = useSelector((state) => state.session.user);
  const posts = useSelector((state) => state.posts);
  const [editable, isEditable] = useState(false);
  const [isPostLoaded, setIsPostLoaded] = useState(false);
  const post = posts[postId];
  const [description, setDescription] = useState(post.description);
  const dispatch = useDispatch();

  const handleEdit = (id, description) => {
    dispatch(editPost(id, description));
  };

  // if (isPostLoaded) {
  //   const editableDescription = document.getElementById(
  //     "post-description-edit"
  //   );
  //   isEditable("true");
  //   editableDescription.addEventListener("focusout", async (e) => {
  //     e.preventDefault();
  //     setDescription(editableDescription.innerHTML());
  //     handleEdit(postId, description);
  //   });
  // }

  const handleDelete = (id) => {
    dispatch(deletePost(id));
    setShowModal(false);
  };
  // useEffect(() => {
  //   setIsPostLoaded(true);
  // }, []);

  return (
    <>
      <div id="post-modal-container">
        <div id="post-modal-image-container">
          <div id="post-modal-image-wrapper">
            <div id="inner-div">
              <img src={post["photos"]} alt=""></img>
            </div>
          </div>
        </div>
        <div id="post-modal-right-container">
          <div id="top-right-container" className="right-column-div">
            <div>
              <div id="profile-pic-holder">
                <img id="profile-pic" src={post.profile_image} alt=""></img>
              </div>
            </div>
            <div>{post.username}</div>
            <div>
              {post.user_id === sessionUser.id && (
                <button onClick={() => isEditable(true)}>Edit</button>
              )}{" "}
              {editable && (
                <div className="edit-post">
                  <textarea
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    className="edit-description-input"
                  />
                  <button
                    className="submit-edit"
                    onClick={() => handleEdit(postId, description)}
                  >
                    Submit
                  </button>
                </div>
              )}
              {post.user_id === sessionUser.id && (
                <button onClick={() => handleDelete(postId)}>Delete</button>
              )}
            </div>
          </div>

          <div className="right-column-div" id="post-description-edit">
            {post.description}
          </div>

          <div className="right-column-div">
            <Comment post_id={postId} />
          </div>
          <div className="right-column-div">Button Bar</div>
          <div className="right-column-div">
            {post.likes} {post.likes === 1 ? "like" : "likes"}
          </div>
          <div className="right-column-div">New Comment Form</div>
        </div>
      </div>
    </>
  );
}
export default DisplayPost;
