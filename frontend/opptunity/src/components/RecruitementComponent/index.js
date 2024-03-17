
import './style.css'
import profileImg from './profile_image.jpg'
const RecruitementComponent = () => {
  return (
    <section className='recruitement'>
      <div className='recruiterdiv'>
        <img src={profileImg}></img>
        <div>
           <p>Albert Flores</p>
           <p>Recruitement Manager</p>
        </div>
        <div className='dash'></div>

      </div>
      <div className='recruiters'>
        <div className='rts'>
          <h3>Recruitement team</h3>
          <p>SEE ALL  &gt;</p>
        </div>


        <div className='recruiterprofile'>
        <div className='profile'>
        <img src={profileImg}></img>
        <div >
           <p>Albert Flores</p>
           <p>Recruitement Manager</p>
        </div>
        </div>
        <div >
           <p style={{color: 'black'}}><b>Interviewer</b></p>
           <p>Toranto</p>
        </div>

      </div>
      <div className='recruiterprofile'>
        <div className='profile'>
        <img src={profileImg}></img>
        <div >
           <p>Albert Flores</p>
           <p>Recruitement Manager</p>
        </div>
        </div>
        <div >
           <p style={{color: 'black'}}><b>Interviewer</b></p>
           <p>Toranto</p>
        </div>

      </div>
      <div className='recruiterprofile'>
        <div className='profile'>
        <img src={profileImg}></img>
        <div >
           <p>Albert Flores</p>
           <p>Recruitement Manager</p>
        </div>
        </div>
        <div >
           <p style={{color: 'black'}}><b>Interviewer</b></p>
           <p>Toranto</p>
        </div>

      </div>
      

      </div>
  


  </section> 
  )
}
export default RecruitementComponent