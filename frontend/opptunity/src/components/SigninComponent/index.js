
import './style.css'
import axios from 'axios';
import  { useState } from 'react'
const SigninComponent = () => {
    const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loginstate,setLoginstate]=useState('')
  async function login() {
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/signin',{
        "email":email,
        "password":password
      });
      if (response.data==true)
      window.location.href = '/adddetails';
      else
        setLoginstate('invalid email/password')

  
      console.log('Login successful:', response.data);
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
          <button   className='submit' onClick={login}>sign in</button>
          </td>
        </tr>
        <tr>
          <td>
            <p style={{color:'red'}}>{loginstate}</p>
          </td>
        </tr>
      </table>
   
    <div className="login-redirect">
      <p>Don't have an account? <a href="/signup">Create free account</a></p>
    </div>
  </section> 
  )
}
export default SigninComponent