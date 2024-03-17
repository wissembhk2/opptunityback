import './App.css';
import EmailConfirmationPage from './pages/EmailConfirmation';
import SignUpPage from './pages/Signup';
import AddDetailsPage from './pages/AddDetails';
import {BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import SignInPage from './pages/Signin';
function App() {
  return (
   <Router>
    <Routes>
      <Route path='/signup' element={<SignUpPage/>}/>
    </Routes>
    <Routes>
      <Route path='/signin' element={<SignInPage/>}/>
    </Routes>
    <Routes>
      <Route path='/emailconfirmation' element={<EmailConfirmationPage/>}/>
    </Routes>
    <Routes>
      <Route path='/adddetails' element={<AddDetailsPage/>}/>
    </Routes>
   </Router>
  );
}

export default App;
