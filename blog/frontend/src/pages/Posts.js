import React from "react";
import ReactDOM from "react-dom";
import { Link } from "react-router-dom";

class Posts extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            posts: [],
            loaded: false,
            nextPage: undefined,
        };
    }

    componentDidMount(){
        fetch('http://127.0.0.1:8000/blogposts/') // this == self
          .then(response => {
            if (response.status === 200) {
              return response.json();
            }
          })
          .then(data => this.setState({ posts: data.results, loaded: true, nextPage: data.next, }));
    }

    handleNewData = () => {
        if (this.state.nextPage == null) {
            return
        }
        fetch(this.state.nextPage)
            .then(response => {
                if (response.status === 200) {
                    return response.json();
                }
            })
            .then(data => this.setState(
                (prevState)=>({posts: [...prevState.posts, ...data.results], loaded: true, nextPage: data.next,})
            ))
    }

    render() {
        return (
            <div className="container">
                <div className="post-conteiner-line">
                    {this.state.loaded ?
                        this.state.posts.map(post =>
                            <React.Fragment>
                                <div className="post-container-header">
                                    <Link to={'/'+post.id}>{post.title}</Link>
                                </div>
                                <div className="post-container-content">
                                    {post.content}
                                    <div className="post-date">
                                        {post.created_at}
                                    </div>
                                </div>
                            </React.Fragment>
                        ):
                    <p>Loading</p>}
                </div>
                <button onClick={ this.handleNewData }> Next </button>
            </div>
        )
    }
}

export default Posts
