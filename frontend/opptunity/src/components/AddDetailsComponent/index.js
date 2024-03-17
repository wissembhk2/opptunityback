
import './style.css'
const AddDetailsComponent = () => {
  return (
    <section className="signup-section">
    <h2>Add Details</h2>
    <p>Clarity gives you the blocks and components you need to create a truly professional website.</p>
    <form>
      <table>
        <tr>
          <td>
            <label>Date of Birth</label>
          <input type="date"  />
          </td>
        </tr>
        <tr>
          <td >
          <label>Gender</label>
          <input type="email"  />
          </td>
        </tr>
        <tr>
          <td>
          <label>Language</label>
          <input type="password"  />
          </td>
        </tr>
        <tr>
          <td>
          <button   className='submit'> submit</button>
          </td>
        </tr>
      </table>
    </form>
    

  </section> 
  )
}
export default AddDetailsComponent