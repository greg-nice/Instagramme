import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

const Post = ({
  id,
  user_id,
  description,
  username,
  likes,
  comments,
  photos,
}) => {
  console.log("url", photos);
  return (
    <div className="post-box">
      <div>{username}</div>
      <div className="photo">
        <img src={photos} alt="post-photo" />
      </div>
      <div className="description">{description}</div>
      <div className="likes">{likes}</div>
      <div className="comments">{comments}</div>
    </div>
  );
};

export default Post;
