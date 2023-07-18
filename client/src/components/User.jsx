import React, {useContext, useEffect} from 'react'
import { useParams } from "react-router-dom"
import Context from "./Context"



function User() {

    // const params = useParams()
    
    const {user, setUser} = useContext(Context)
    
    
    // useEffect(() => {
    //     fetch(`/api/users/${user.id}`)
    //     .then(res => res.json())
    //     .then(user => setUser(user))
    // },[user])  
    // console.log(user)
    
console.log(user)


  return (
    <div>
        <h2>Welcome, </h2>
        {/* <img src={user.image} alt={user.name}></img>
        <p>{user.name}</p>
        <p>{user.bio}</p> */}
        {/* <p>{user.completed_prompts}</p> */}
    </div>
  )

}

export default User