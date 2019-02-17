import React from 'react';
import ReactDOM from "react-dom";
import App from "./App";

// const e = <LikeScoob />;

// class LikeScoob extends React.Component {
//   constructor(props) {
//     super(props);
//     this.state = { liked: false };
//   }

//   render() {
//     return (<Button onClick={this.showView}>
//      'View' </Button> 
//     );
//   }

//   showView() {
//     // download the view
//   }

// }

// ReactDOM.render(e, document.getElementById('scoob_snack'));

ReactDOM.render(<App />, document.getElementById("content"));