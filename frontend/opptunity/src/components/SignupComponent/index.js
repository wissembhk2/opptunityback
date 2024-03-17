
import './style.css'
import axios from 'axios';
import { useState } from 'react';
import { redirect } from 'react-router-dom';
const SignupComponent = () => {
  const [email, setEmail] = useState('');
  const [name, setName] = useState('');

  const [password, setPassword] = useState('');
  async function signup() {
    console.log(email,password,name)
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/signup',
      {
        "name":name,
        "email":email,
        "password":password

      });
  
      console.log('Sign up successful:', response);
      window.location.href = '/emailconfirmation';
      // Handle successful login, e.g., store the token, redirect the user
  
    } catch (error) {
      if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        console.error('Login failed:', error.response.data);
        // Handle login failure, e.g., show an error message
      } else if (error.request) {
        // The request was made but no response was received
        console.error('No response:', error.request);
      } else {
        // Something happened in setting up the request that triggered an Error
        console.error('Error:', error.message);
      }
    }
  }
  return (
    <section className="signup-section">
    <h2>Welcome!</h2>
    <p>Clarity gives you the blocks and components you need to create a truly professional website.</p>
      <table>
        <tr>
          <td>
            <label>Name</label>
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
          </td>
        </tr>
        <tr>
          <td >
          <label>Email</label>
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
          </td>
        </tr>
        <tr>
          <td>
          <label>Password</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          </td>
        </tr>
        <tr>
          <td>
          <button   className='submit' onClick={signup}> submit</button>
          </td>
        </tr>
      </table>
    <div className="social-signup">
     <p>OR</p> 
     <div>
        <button className="socialmedia-signup">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Google_%22G%22_logo.svg/2048px-Google_%22G%22_logo.svg.png"></img>
          Google Sign Up
          </button>
          <button className="socialmedia-signup">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Microsoft_logo.svg/2048px-Microsoft_logo.svg.png"></img>
          Microsoft Sign Up
          </button>
      </div>
    </div>
    <div className="login-redirect">
      <p>Already have an account? <a href="/signin">Log In</a></p>
    </div>
  </section> 
  )
}
export default SignupComponent