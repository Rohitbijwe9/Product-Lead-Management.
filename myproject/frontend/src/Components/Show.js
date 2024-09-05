import axios from 'axios';
import React from 'react'
import { useEffect,useState } from 'react'
import { Link, useNavigate } from 'react-router-dom';

function Show() {

    const[user,setUser]=useState([])

    async function fetchdata()
    {
      const result = await axios.get('http://127.0.0.1:8000/product-api/')

      setUser(result.data)
      



    }

    useEffect(()=>{fetchdata()},[])
  return (
    <>
    <table className='table table-stiped'>
        <thead>
            <tr>
                <th>PRODUCT NAME</th>
                <th>DESCRIPTION</th>
                <th>PRICE</th>
                <th>CREATE DATE</th>
                <th>UPDATE DATE</th>
                <th>ACTION</th>




            </tr>
        </thead>
        <tbody>
            {user.map(obj=>{return(
                <tr>
                    <td>{obj.name}</td>
                    <td>{obj.description}</td>
                    <td>{obj.price}</td>
                    <td>{obj.created_at}</td>
                    <td>{obj.updated_at}</td>
                    <td>
                        <Link to='#'>
                        <button class='btn btn-warning' type='button' >UPDATE</button>
                        </Link>
                        <Link to='#'>
                        <button class='btn btn-danger' type='button' >Delete</button>
                        </Link>

                    </td>





                </tr>

            )})}
            
        </tbody>
    </table>
    </>
  )
}
export default Show