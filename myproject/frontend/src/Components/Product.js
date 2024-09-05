import React from 'react'
import {useForm} from 'react-hook-form';
import axios from 'axios'
import { useNavigate } from 'react-router-dom';

function Product() {

  const{register,handleSubmit}=useForm();
  const redirect=useNavigate();


  function add(data)
  {
    axios.post('http://127.0.0.1:8000/product-api/',data)
    redirect('/show')
    
  }

  
  
  return (
   <>
   <form onSubmit={handleSubmit(add)}>
    <br/><br/>
    <label>Product Name</label>
    <input type='text' className='form-control' placeholder='enter product name'
    {...register('name')}/><br/>

    <label>Description</label>
    <input type='text' className='form-control' placeholder='enter email'
    {...register('description')}/><br/>

    
    <label>Price</label>
    <input type='text' className='form-control' placeholder='enter phone number'
    {...register('price')}/><br/>


    <input type='submit' value={'ADD DATA'} className='btn btn-primary'/><br/><br/>







    
    






   </form><br/><br/>



   </>
  )
}

export default Product