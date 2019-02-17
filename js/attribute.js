import Reat, {Component} from 'react';

var url = "localhost:8000/init?upload=[file]&header=[fileHeader]"
class SearchList extends Component {
    constructor(props){
        super(props);
        this.state = {
            attrList:[],
        };
    }
    
    componentDidMount(){
        fetch(url){
            .then(respones => response.json())
            .then(data => this.setState({attrList: data}))
        }
    }
    handler(attr){
        this.setState(({attrList}) => {
            const newList = new Set(attrList);
            newList.delete(attr);
            return {attrList: Array.from(newList)}
        })
    }
    render() {
        const {attrList} = this.state;
        const attributeList = attrList.map((attr) =>
            <SearchEntry key ={attr} value={attr} handler={this.handler}>
                                           
        )
        return (
            <ul>
            {attributeList}
            </ul>
        )
    }
    
    
}
class SearchEntry extends Component {
    constructor(props){
        super(props);
        this.state={
            isChecked:false;
        };
        this.removeItem = this.removeItem.bind(this);
        this.checkItem = this.checkItem.bind(this);
    }
    checkItem(){
        if(this.state.isChecked){
            AttrList.removeItem(this.props.value);
            this.setState({isChecked:false})
        }
        else{
            this.setState({isChecked:true});
            AttrList.addItem(this.props.value);
        }
    }
    removeItem(){
        if(this.state.isChecked){
            AttrList.removeItem(this.props.value);
        }
        this.props.handler(this.props.value);
        
    }
    render(){
        
    }
    

    
    
}
fetch(url){
    .then((resp) => resp.json())
    .then(function(data){
        
    })
       
})/////

var attributes = ["sepal_length","sepal_width","petal_length","petal_width","species"];
//empty array to store attributes

//do some request to store the attributes

var attrListItems = attributes.map((attributes) =>
  <li>{attributes}</li>                                  
);

ReactDOM.render(
    <ul>{listItems}</ul>,
    document.getElementById("attributes")
    
);