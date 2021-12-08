import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import * as sessionActions from "../../store/session";
import '../ProfileButton/ProfileButton.css'


function ProfileButton({ user }) {
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const [isLoaded, setIsLoaded] = useState(false);

  // useEffect(() => {
  //   dispatch(sessionActions.restoreUser()).then(() => setIsLoaded(true));
  // }, [dispatch]);

  const openMenu = () => {
    if (showMenu) return;
    setShowMenu(true);
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = () => {
      setShowMenu(false);
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const logout = (e) => {
    e.preventDefault();
    dispatch(sessionActions.logout());
  };

  return (
    <div className="buttonContainer"
    onClick={openMenu}
    >
      <div className="hamburgerMenuContainer">
      <i class="fas fa-bars"></i>
      </div>
      <div className="profileImageContainer">
      {user
      ? user.imageURL
      ? <img src={user.imageURL} className="profileImage"></img>
      : <i className="fas fa-user-circle"></i>
      : <i className="fas fa-user-circle"></i>
      }
      </div>
        <div className="dropdownContent">
          {user ?
          <>
            <a onClick={logout} href="/">
            Log Out
            </a>


            </> :
            <div className="modalLinks">

            </div>
          }
        </div>
    </div>
  );
}

export default ProfileButton;
