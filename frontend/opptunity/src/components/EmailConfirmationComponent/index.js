
import './style.css'
import sendmail from "./sendmail.png"
const EmailConfirmationComponent = () => {
  return (
    <section className="signup-section">
    <h2>Email Confirmation</h2>
    <p>We have sent an email to xyz@gmail.com. Please verify your email address to go further. Follow the steps down in the email</p>
    <img src={sendmail}></img>
    <div className="login-redirect">
    <p>Didn't receive an email ? <a href="#">Resend it</a></p>
    <p>Go to  <a href="/signin">login page</a></p>

    </div>


  </section> 
  )
}
export default EmailConfirmationComponent