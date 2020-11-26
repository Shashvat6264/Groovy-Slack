import React from 'react';
import axios from 'axios';
import Articles from "../components/Article";

const data = [
  'Racing car sprays burning fuel into crowd.',
  'Japanese princess to wed commoner.',
  'Australian walks 100km after outback crash.',
  'Man charged over missing wedding girl.',
  'Los Angeles battles huge wildfires.',
];

class ArticleList extends React.Component{
    state = {
        articles: []
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/events/')
            .then(res => {
                this.setState({
                    articles: res.data
                });
                console.log(res.data);
            })
    }

    render(){
        return(
              <Articles data={this.state.articles} />
        );
    }
}

export default ArticleList;