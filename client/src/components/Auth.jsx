import React, { useState, useContext } from 'react';
import {useFormik} from "formik";
import * as yup from "yup";
import {useNavigate} from "react-router-dom"
import {TextField, Button, Typography} from '@mui/material'


function Auth({updateUser}){
    //5. sign up/log in/log out
    const [signup, setSignup] = useState(true)
    const [error, setError] = useState(null)
    const navigate = useNavigate()
    const toggleSignup = () => setSignup(prev => !prev);
     
    const schema = yup.object().shape({
        name: yup.string(),
        username: yup.string(),
        email: yup.string(),
        password: yup.string(),
        bio: yup.string(),
        image: yup.string()
    })


  //create formik instance
    const formik = useFormik({
      //initial values form
        initialValues: {
            name: "",
            username: "",
            email: "",
            password: "",
            bio: "",
            image: ""
        },
      //yup schema for validation
        validationSchema: schema,
      //submit callback
        onSubmit: (values, actions) => {
            fetch( signup ? "/api/login" : "/api/signup", {
                method: "POST",
                headers: {
                    "content-type" : "application/json"
                },
                body: JSON.stringify(values)
            }).then (res => {
                if(res.ok){
                    res.json().then(user => {
                        actions.resetForm()
                        updateUser(user)
                        navigate("/home")
                    })
                } else{
                    console.log("oops")
                }
            })
        }

    })


    return (
       <section className="page">
        
            { signup ? (
             <form onSubmit={formik.handleSubmit}>
             {/* <label> Username: */}
             <TextField
             variant="outlined"
             sx={{margin: 3}}
             placeholder="username"
             type={"text"}
             name="username" 
             onChange={formik.handleChange}
             value={formik.values.username}
             onBlur={formik.handleBlur}/>
             {formik.touched.username && formik.errors.username ? (
             <h3>{formik.errors.username}</h3>
             ) : ("")}
             {/* </label> */}
             {/* <label> Password */}
                 <TextField
             variant="outlined"
             sx={{margin: 3}}
             placeholder="password"
             type={"password"} 
              name="password" 
              onChange={formik.handleChange}
              value={formik.values.password}
              onBlur={formik.handleBlur}/>
             {formik.touched.password && formik.errors.password ? (
              <h3>{formik.errors.password}</h3>
              ) : ("")}
             {/* </label> */}
             {/* <input type="submit" value="Log In" /> */}
             <Button color="secondary" variant="outlined" sx={{margin: 3}} placeholder="Log In!" type="submit">Log In!</Button>
             {error ? <label style={{ color: "red" }}>{error}</label> : ""}
         </form>
         ) : (
            <form onSubmit={formik.handleSubmit}>
            {/* <label> Name: */}
            <TextField
            variant="outlined"
            sx={{margin: 3}}
            placeholder="name"
            type={"text"} 
            name="name" 
            onChange={formik.handleChange}
            value={formik.values.name}
            onBlur={formik.handleBlur}/>
            {/*this is the onBlur*/}
            {formik.touched.name && formik.errors.name ? (
            <h3>{formik.errors.name}</h3>
            ) : ("")}
            {/* </label> */}
            {/* <label> Username: */}
            <TextField
            variant="outlined"
            sx={{margin: 3}}
            placeholder="username"
            type={"text"}
            name="username" 
            onChange={formik.handleChange}
            value={formik.values.username}
            onBlur={formik.handleBlur}/>
            {formik.touched.username && formik.errors.username ? (
            <h3>{formik.errors.username}</h3>
            ) : ("")}
            {/* </label> */}
            {/* <label> Email: */}
            <TextField
            variant="outlined"
            sx={{margin: 3}}
            placeholder="email"
            type={"email"}
            name="email" 
            onChange={formik.handleChange}
            value={formik.values.email}
            onBlur={formik.handleBlur}/>
            {formik.touched.email && formik.errors.email ? (
            <h3>{formik.errors.email}</h3>
            ) : ("")}
            {/* </label> */}
            {/* <label> Password */}
            <TextField
            variant="outlined"
            sx={{margin: 3}}
            placeholder="password"
            type={"password"} 
            name="password" 
            onChange={formik.handleChange}
            value={formik.values.password}
            onBlur={formik.handleBlur}/>
            {formik.touched.password && formik.errors.password ? (
            <h3>{formik.errors.password}</h3>
            ) : ("")}
            {/* </label> */}
            {/* <label> Bio: */}
            <TextField
            variant="outlined"
            sx={{margin: 3}}
            placeholder="bio"
            type={"text"} 
            name="bio" 
            onChange={formik.handleChange}
            value={formik.values.bio}
            onBlur={formik.handleBlur}/>
            {formik.touched.bio && formik.errors.bio ? (
            <h3>{formik.errors.bio}</h3>
            ) : ("")}
            {/* </label> */}
            {/* <label> Image: */}
            <TextField
            variant="outlined"
            sx={{margin: 3}}
            placeholder="image"
            type={"text"} 
            name="image" 
            onChange={formik.handleChange}
            value={formik.values.image}
            onBlur={formik.handleBlur} />
            {formik.touched.image && formik.errors.image ? (
            <h3>{formik.errors.image}</h3>
            ) : ("")}
            {/* </label> */}
            <Button color="secondary" variant="outlined" sx={{margin: 3}} placeholder="Join!" type="submit">Join!</Button>
            {/* <input type="submit" value="Join!" /> */}
            </form>
           
            )}
            <section>
				<Typography  color="secondary" sx={{marginLeft: "25px"}}>{signup ? "Not a member?" : "Already have an account?"}</Typography>
				<Button color="secondary" variant="outlined" sx={{margin: 3}} onClick={toggleSignup}>
					{signup ? "Sign Up" : "Log In"}
				</Button>
			</section>
        </section>
    )
}

export default Auth