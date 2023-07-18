import { red } from '@mui/material/colors';
import { createTheme } from '@mui/material/';
// A custom theme for this app
const theme = createTheme({
  spacing: 10,
  palette: {
    type: 'light',
    primary: {
      main: '#e9cfb4', //backPeach
      light: '#FFAE99', //cardBackPink
      dark: '#D76E53', //headerBackPink
    },
    secondary: {
      main: '#7E6936', //headerBackGreen
      light: '#9D8853', //formBackGreen
      dark: '#967C3D', //pageBackGreen
    },
    error: {
      main: red.A400,
    },
  //   background: {
  //     default: '#FFAE99',
  //   },
  // },
  // overrides: {
  //   MuiPaper: {
  //     root: {
  //       padding: '20px 10px',
  //       margin: '10px',
  //       backgroundColor: '#E7CAAC', // 5d737e
  //     },
  //   },
  //   MuiButton: {
  //     root: {
  //       margin: '5px',
  //     },
  //   },
  // },
  // components: {
  //   MuiTypography: {
  //     defaultProps: {
  //       variantMapping: {
  //         h1: 'h2',
  //         h2: 'h2',
  //         h3: 'h2',
  //         h4: 'h2',
  //         h5: 'h2',
  //         h6: 'h2',
  //         subtitle1: 'h2',
  //         subtitle2: 'h2',
  //         body1: 'span',
  //         body2: 'span',
  //       },
  //     },
  //   },
  },
});
export default theme;