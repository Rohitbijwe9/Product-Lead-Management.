import logo from './logo.svg';
import './App.css';
import Navbar from './Components/Layout/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Product from './Components/Product';
import Show from './Components/Show';
import Signup from './Components/Auth/Signup';



function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
      <Route path='product/' element={<Product />} />
      <Route path='show/' element={<Show/>}/>
      <Route path='signup/' element={<Signup/>}/>
        
      </Routes>
    </Router>
  );
}

export default App;
