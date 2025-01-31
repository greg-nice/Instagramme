// import { csrfFetch } from "./csrf";
const GET_COMMENTS = "/comments/getComments";
const ADD_COMMENT = "/comments/addComment";
const UPDATE_COMMENT = "/comments/updateComment";
const REMOVE_COMMENT = "/comments/removeComment";

const getComments = (payload) => ({
  type: GET_COMMENTS,
  payload: payload,
});

const addComment = (payload) => ({
  type: ADD_COMMENT,
  payload,
});

const updateComment = (payload) => ({
  type: UPDATE_COMMENT,
  payload,
});

const deleteComment = (id) => ({
  type: REMOVE_COMMENT,
  id,
});

export const getAllComments = (id) => async (dispatch) => {
  const response = await fetch(`/api/posts/${id}/comments`);
  if (response.ok) {
    const data = await response.json();
    dispatch(getComments(data));
  }
};

export const addAComment = (pid, id, comment) => async (dispatch) => {
  const response = await fetch(`/api/posts/${pid}/comments`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ id, comment }),
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(addComment(data));
    return data;
  }
};

export const updateAComment = (id, cid, content) => async (dispatch) => {
  const response = await fetch(`/api/posts/${id}/comments/${cid}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ content }),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(updateComment(data));
    return data;
  }
};

export const deleteAComment = (pid, id) => async (dispatch) => {
  const response = await fetch(`/api/posts/${pid}/comments/${id}`, {
    method: "DELETE",
  });

  if (response.ok) {
    dispatch(deleteComment(id));
  }
};

const initialState = {};
const commentReducer = (state = initialState, action) => {
  let newState = {};
  switch (action.type) {
    case GET_COMMENTS:
      for (let comment in action.payload) {
        newState[comment] = action.payload[comment];
      }
      return newState;
    case ADD_COMMENT:
      newState = {
        ...state,
        [action.payload.id]: action.payload,
      };
      return newState;
    case UPDATE_COMMENT:
      newState = { ...state };
      newState[[action.payload.id]] = action.payload;
      return newState;
    case REMOVE_COMMENT:
      delete state[action.id]
      newState = {...state};
      return newState
    default:
      return state;
  }
};

export default commentReducer;
