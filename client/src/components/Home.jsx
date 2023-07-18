import React from 'react'
import Container from '@mui/material/Container'
import Grid from '@mui/material/Grid'
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import ImageList from '@mui/material/ImageList';
import {ImageListItem, ImageListItemBar, IconButton} from '@mui/material';


function srcset(image, width, height, rows = 1, cols = 1) {
  return {
    src: `${image}?w=${width * cols}&h=${height * rows}&fit=crop&auto=format`,
    srcSet: `${image}?w=${width * cols}&h=${
      height * rows
    }&fit=crop&auto=format&dpr=2 2x`,
  };
}
function Home() {
  return (
    <ImageList
      sx={{
        marginTop: "200px",
        width: 1400,
        height: 1260,
        // Promote the list into its own layer in Chrome. This costs memory, but helps keeping high FPS.
        transform: 'translateZ(0)',
      }}
      rowHeight={560}
      gap={1}
    >
      {itemData.map((item) => {
        const cols = item.featured ? 2 : 1;
        const rows = item.featured ? 2 : 1;

        return (
          <ImageListItem key={item.img} cols={cols} rows={rows}>
            <img
              {...srcset(item.img, 250, 200, rows, cols)}
              alt={item.title}
              loading="lazy"
            />
            <ImageListItemBar
              sx={{
                background:
                  'linear-gradient(to bottom, rgba(0,0,0,0.7) 0%, ' +
                  'rgba(0,0,0,0.3) 70%, rgba(0,0,0,0) 100%)',
              }}
              title={item.title}
              position="top"
              actionIcon={
                <IconButton
                  sx={{ color: 'white' }}
                  aria-label={`star ${item.title}`}
                >
                  {/* <StarBorderIcon /> */}
                </IconButton>
              }
              actionPosition="left"
            />
          </ImageListItem>
        );
      })}
    </ImageList>
  );
}

const itemData = [
  {
    img: 'https://i.pinimg.com/originals/1f/56/50/1f5650e0f275785b9b6bde01197a208a.jpg',
    featured: true,
  },
  {
    img: 'https://mymodernmet.com/wp/wp-content/uploads/2017/08/nature-medleys-mushrooms-jill-bliss-1.jpg'
    // img: 'https://i.pinimg.com/originals/9d/d3/44/9dd3446af571b9da8277c15777382bd2.jpg',
  },
  {
    img: 'https://static.boredpanda.com/blog/wp-content/uploads/2017/08/mushrooms-nature-medley-photos-jill-bliss-8-59895e2b8cb8e__700.jpg'
    // img: 'https://as1.ftcdn.net/v2/jpg/05/07/24/00/1000_F_507240001_2VfDNTo5co3ZRZsuYPzd2EsKKQUO9iU0.jpg'
    // img: 'https://media.newyorker.com/photos/609068772f5b0e07ae1843c3/master/w_1600%2Cc_limit/Rosner-Mushrooms-leccium.jpg'
  },
  {
    img: 'https://static.skillshare.com/uploads/project/241552/cover_800_4e59304c544264206e97d6669b8a8bd1.jpg',
    // img: 'https://images.squarespace-cdn.com/content/v1/5861e6ec414fb5a4e21a5ff2/1551046107942-F2B7NNR0I09DGVL93Q93/Good+Morning+Juice+web+tumblr.jpg?format=500w',
    // img: 'https://images.squarespace-cdn.com/content/v1/5861e6ec414fb5a4e21a5ff2/1503902678443-EXG2CARJCVWOL7GFIPCC/Garden+Desert+tumblr+web.jpg?format=1500w',
    // img: 'https://www.thephotoargus.com/wp-content/uploads/2019/01/fungi30.jpg'
  },
  {
    img: 'https://www.treehugger.com/thmb/5gvna5sA4OhNEdNLvk4GjL9RVc8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/amethyst-deceiver-mushrooms-1329276825-643a3613450e4c9289e60e870e5a0da7.jpg',
    // img: 'https://i.pinimg.com/736x/63/6b/d1/636bd1095b3600436b327c89593691ba.jpg'
  },
  {
    img: 'https://d3ui957tjb5bqd.cloudfront.net/uploads/2021/05/28113203/SP1cSEE0.png',
    featured: true,
  },
  {
    img: 'https://petapixel.com/assets/uploads/2020/10/mush5-800x533.jpg'
  },
  {
    img: 'https://cdn.pixabay.com/photo/2017/09/25/21/13/mushrooms-2786789_1280.jpg'
  },
  {
    img: 'https://www.thephotoargus.com/wp-content/uploads/2019/01/fungi12.jpg',
    // img: 'https://live.staticflickr.com/717/31455156794_cec433173d_b.jpg'
  },
  {
    img: 'https://as2.ftcdn.net/v2/jpg/04/42/14/19/1000_F_442141969_hGnUo2IJMVStqjHQ4xI7dKdJFA6fseki.jpg'
    // img: 'https://i.pinimg.com/originals/ce/21/41/ce2141e9c96d362c3ead753ad98388e1.jpg'
  
  },
  {
    img: 'https://i.pinimg.com/originals/f1/c1/18/f1c1183cec0ceecf9e3c190b40223581.jpg'
  },
  {
    img: 'https://i.pinimg.com/736x/8e/01/30/8e0130da1f3917ff1422d7fc202476d1.jpg'
  },
];



export default Home
    // <div className="background">
    //     <h1>micelio</h1>
    //     <img></img>
        
    //     <img
    //     src="https://www.designboom.com/wp-content/uploads/2021/05/alison-pollack-mushroom-photography-designboom-fb.jpg" 
    //     alt="micelio">
    //     </img>
    // </div>