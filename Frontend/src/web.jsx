import './web.css'
import Login from './login.jsx'
import { Link,useNavigate } from 'react-router-dom';

function WebFrame() {
  const navigate =useNavigate();
  const handleclick = () =>{
    navigate(Login);
  };
    

  return (
    <>
      <div className='web'>
        <h2 className='text'>Event Planner</h2>
        <p className='para'>
          <Link to="/login">Login in</Link>
          <a href="">About</a>
          <a href="">Contact</a>
        </p>
        <div className='font'>
          <h1 className='plan'>Plan Your Events</h1>
          <h3>Discover the perfect venue, decoration and caterer for your events</h3>
        </div>
        <div className='searchbar'>
          <input type="text" placeholder='search for venues, decorators, caterers etc.,' />
          <button>Search</button>
        </div>
      </div>
      

    </>
  );

}

export default WebFrame;
