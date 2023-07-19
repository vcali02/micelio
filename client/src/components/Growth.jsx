import React, {useContext, useState, useEffect} from 'react'
import Context from "./Context"

function Growth() {
  const {user, setUser} = useContext(Context)
  const [completedByUser, setCompByUser] = useState([])
  console.log(user)


  useEffect(() => {
    if (user) {
      fetch(`/api/completed_by_user/${user.id}`)
        .then((response) => response.json())
        .then((data) => {
          setCompByUser(data);
        })
        .catch((error) => console.log(error));
    }
  }, [user]);

 

  return (
    <div className="page">
      <p>{user.completed_prompts}</p>
    </div>
  )
}

export default Growth