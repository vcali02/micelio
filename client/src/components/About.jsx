import React from 'react'
import {Link } from "react-router-dom"
import {CardActionArea, CardActions } from '@mui/material';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import {Button, Box, Paper, Grid, Typography, CssBaseline, ThemeProvider} from '@mui/material';
import Container from '@mui/material/Container'

function About() {
  return (
    <Container sx={{marginLeft: "auto", marginTop: "auto"}}>
    <Card sx={{ maxWidth: 1000, marginTop: "250px", marginBottom: "50px" }}>
      <CardActionArea>
        <CardMedia
          component="img"
          height="140"
          image="https://www.designboom.com/wp-content/uploads/2021/05/alison-pollack-mushroom-photography-designboom-fb.jpg"
          alt="micelio"
        />
        <CardContent>
          <Typography gutterBottom variant="h5" component="div">
          About
          </Typography>

          <Typography variant="body2" color="text.secondary">
          In a world with over 7 billion people, it is unsurprising the chaos that ensues. With such a massive number in mind, it is overwhelming to fathom a way to tame the masses into peace.
          </Typography>

          <Typography variant="body2" color="text.secondary">
          Fortunately, humanity has an exceptional teacher in nature. In the depths of despair, mycelium emerges to feed on death to birth life. It advocates for those in need through communication within the earth and effective routing of resources.
          </Typography>

          <Typography variant="body2" color="text.secondary">
          Mycelium represents life, death, and peace all through its own actions. Humanity may not be able to control the rest of humanity, but we can learn to control ourselves. We can grow in the presence of doom, we can choose peace through our actions. We have the incredible privilege to experience existence through the lense of a human. This is not to be mistaken as "easy," but regarded as an opportunity to experience a spectrum of what it is to be alive. Inherently, this spectrum requires the ability to face death, and if you allow yourself, birth life.
          </Typography>

          <Typography variant="body2" color="text.secondary">
          Explore your hidden dimensions through Micelio. Discover the power within you to develop yourself into the being you envision yourself to be, and watch your life change as your growth inspires others to do the same.
          </Typography>



          <Typography gutterBottom variant="h5" component="div">  
          Root of Growth
          </Typography>

          <Typography variant="body2" color="text.secondary">
          Micelio is influenced by the concept that we have four pillars through which we can access our power and peace. These pillars are philosophies of life.
          </Typography>

          <Link to = {`/pillars`}>
          <Typography gutterBottom variant="h5" component="div">
          Be Impeccable with Your Word
          </Typography>
          </Link>
          
          <Typography variant="body2" color="text.secondary">
          The first pillar is the umbrella for the rest. It is through this pillar that you create the foundation for growth.
          </Typography>

          <Link to = {`/pillars`}>
          <Typography gutterBottom variant="h5" component="div">
          Don't Take Anything Personally
          </Typography>
          </Link>

          <Typography variant="body2" color="text.secondary">
          The second pillar challenges your perspective of the first pillar by putting you in another person's shoes.
          </Typography>

          <Link to = {`/pillars`}>
          <Typography gutterBottom variant="h5" component="div">
          Don't Make Assumptions
          </Typography>
          </Link>

          <Typography variant="body2" color="text.secondary">
          he third pillar encourages you to take courage and gather information and knowledge through asking questions.
          </Typography>

          <Link to = {`/pillars`}>
          <Typography gutterBottom variant="h5" component="div">
          Always Do Your Best
          </Typography>
          </Link>

          <Typography variant="body2" color="text.secondary">
          The fourth pillar gives you permission to accept yourself.
          </Typography>



          <Typography gutterBottom variant="h5" component="div">
          How it Works
          </Typography>

          <Typography variant="body2" color="text.secondary">
          Micelio is designed to facilitate growth through the four pillars. To get started, log in to your Micelio account and navigate to the pillars page.
          </Typography>

          <Typography variant="body2" color="text.secondary">
          Once you arrive, you will see the pillars displayed with individual descriptions. Select a pillar you want to focus on and Micelio will navigate you to the methods through which you can attain your desired growth.
          </Typography>

          <Typography variant="body2" color="text.secondary">
          You will see the methods associated with the pillar you selected displayed on your page. Here you can pick your preferred method.
          </Typography>

          <Typography variant="body2" color="text.secondary">
          Upon selecting a method, you will see a suggestion for how to apply this method in your life to progress your growth in the pillar of your selection.
          </Typography>

          <Typography variant="body2" color="text.secondary">
          Go about your life applying these exercises and watch your life transform through your commitment to yourself!
          </Typography>



          <Typography gutterBottom variant="h5" component="div">
          Recommended
          </Typography>

          <Typography variant="body2" color="text.secondary">
          Check out our Recommended page for Micelio favorites that can supplement your self exploration and growth alongside Micelio.
          </Typography>
        </CardContent>
      </CardActionArea>
    </Card>
    </Container>
  )
}

export default About
    // <div>
    //     <h1>About</h1>
    //     <p>In a world with over 7 billion people, it is unsurprising the chaos that ensues. With such a massive number in mind, it is overwhelming to fathom a way to tame the masses into peace.</p>
    //     <p>Fortunately, humanity has an exceptional teacher in nature. In the depths of despair, mycelium emerges to feed on death to birth life. It advocates for those in need through communication within the earth and effective routing of resources.</p>
    //     <p>Mycelium represents life, death, and peace all through its own actions. Humanity may not be able to control the rest of humanity, but we can learn to control ourselves. We can grow in the presence of doom, we can choose peace through our actions. We have the incredible privilege to experience existence through the lense of a human. This is not to be mistaken as "easy," but regarded as an opportunity to experience a spectrum of what it is to be alive. Inherently, this spectrum requires the ability to face death, and if you allow yourself, birth life.</p>
    //     <p>Explore your hidden dimensions through Micelio. Discover the power within you to develop yourself into the being you envision yourself to be, and watch your life change as your growth inspires others to do the same.</p>
        
    //     <h2>Root of Growth</h2>
    //     <p>Micelio is influenced by the concept that we have four pillars through which we can access our power and peace. These pillars are philosophies of life.</p>
    //     <Link to = {`/pillars`}>
    //     <h4>Be Impeccable with Your Word</h4>
    //     <p>The first pillar is the umbrella for the rest. It is through this pillar that you create the foundation for growth.</p>
    //     <h4>Don't Take Anything Personally</h4>
    //     <p>The second pillar challenges your perspective of the first pillar by putting you in another person's shoes.</p>
    //     <h4>Don't Make Assumptions</h4>
    //     <p>The third pillar encourages you to take courage and gather information and knowledge through asking questions.</p>
    //     <h4>Always Do Your Best</h4>
    //     <p>The fourth pillar gives you permission to accept yourself.</p>
    //     </Link>

    //     <h2>How it Works</h2>
    //     {/* <ol>
    //       <li>Micelio is designed to facilitate growth through the four pillars. To get started, log in to your Micelio account and navigate to the pillars page.</li>
    //       <li>Once you arrive, you will see the pillars displayed with individual descriptions. Select a pillar you want to focus on and Micelio will navigate you to the methods through which you can attain your desired growth.</li>
    //       <li>You will see the methods associated with the pillar you selected displayed on your page. Here you can pick your preferred method.</li>
    //       <li>Upon selecting a method, you will see a suggestion for how to apply this method in your life to progress your growth in the pillar of your selection.</li>
    //       <li>Go about your life applying these exercises and watch your life transform through your commitment to yourself!</li>
    //     </ol> */}

    //     <p>Micelio is designed to facilitate growth through the four pillars. To get started, log in to your Micelio account and navigate to the pillars page.</p>
    //     <p>Once you arrive, you will see the pillars displayed with individual descriptions. Select a pillar you want to focus on and Micelio will navigate you to the methods through which you can attain your desired growth.</p>
    //     <p>You will see the methods associated with the pillar you selected displayed on your page. Here you can pick your preferred method.</p>
    //     <p>Upon selecting a method, you will see a suggestion for how to apply this method in your life to progress your growth in the pillar of your selection.</p>
    //     <p>Go about your life applying these exercises and watch your life transform through your commitment to yourself!</p>
    //     <h2>Recommended</h2>
    //     <p>Check out our Recommended page for Micelio favorites that can supplement your self exploration and growth alongside Micelio.</p>
    // </div>