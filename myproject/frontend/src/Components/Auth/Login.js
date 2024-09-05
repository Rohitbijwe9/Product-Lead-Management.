import React from 'react'
import {useForm} from 'react-hook-form';
import axios from 'axios'
import { useNavigate } from 'react-router-dom';

function Signup() {

  const{register,handleSubmit}=useForm();


  function add(data)
  {
    axios.post('http://127.0.0.1:8000/signup-api/',data)
    
  }

  
  
  return (
   <>
   <form onSubmit={handleSubmit(add)}>
    <br/><br/>
    <label>Username</label>
    <input type='text' className='form-control' placeholder='enter username'
    {...register('username')}/><br/>

    <label>Password</label>
    <input type='password' className='form-control' placeholder='enter password'
    {...register('password')}/><br/>

    
    <label>Email</label>
    <input type='email' className='form-control' placeholder='enter email'
    {...register('email')}/><br/>


    <input type='submit' value={'SIGNUP'} className='btn btn-primary'/><br/><br/>







    
    






   </form><br/><br/>



   </>
  )
}

export default Signup