
import './style.css'
import logo from './logo.png'
const WelcomeComponent = ({ChildComponent}) => {
  return (
<section className="welcome-section">
<img src={logo} className='logo'></img>
<ChildComponent/>
 <div className="quarter-circle"></div> 
</section>
  )
}
export default WelcomeComponent