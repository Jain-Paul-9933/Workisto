import React from "react";
import { Link } from "react-router-dom";
import { useSelector } from "react-redux";
// import { useNavigate } from "react-router-dom";
import { useDispatch } from "react-redux";
import { clearUSer } from "../../slices/userSlice";

const HomePage = () => {

  const dispatch=useDispatch()
  
  // const navigate=useNavigate()

  const handleLogout=()=>{

    dispatch(clearUSer())
    window.location.href = "/user_login";
    // navigate('/user_login')

  }

  const user=useSelector((state)=>state.user.user) 
  console.log(user)
  return (
    <div>
      <nav className="bg-blue-500 p-4">
        <div className="container mx-auto flex items-center justify-between">
          <Link to="/" className="text-white text-2xl font-kaushan">
            Workisto
          </Link>
          <ul className="flex space-x-4">
            {user ? ( // Check if the user is logged in
              <>
                <li>
                  <Link to="/profile" className="text-white hover:text-gray-200">
                    Hi, {user.username}
                  </Link>
                </li>
                <li>
                  <Link onClick={handleLogout} className="text-white hover:text-gray-200">
                    Logout
                  </Link>
                </li>
              </>
            ) : (
              <>
                <li>
                  <Link
                    to="/user_registration"
                    className="text-white hover:text-gray-200"
                  >
                    Register
                  </Link>
                </li>
                <li>
                  <Link
                    to="/user_login"
                    className="text-white hover:text-gray-200"
                  >
                    Login
                  </Link>
                </li>
              </>
            )}
          </ul>
        </div>
      </nav>

      <div className="container mx-auto mt-8">
        <h1 className="text-3xl font-semibold">Welcome to Workisto</h1>
        <p className="mt-4 text-gray-600">
          Your platform for connecting with skilled professionals.
        </p>
      </div>
    </div>
  );
};

export default HomePage;
