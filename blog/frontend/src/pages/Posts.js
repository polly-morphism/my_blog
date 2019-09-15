import React from "react";
import ReactDOM from "react-dom";
import { Link } from "react-router-dom";

class Posts extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            posts: [],
            loaded: false,
        };
    }

    componentDidMount(){
        fetch('blogposts/') // this == self
          .then(response => {
            if (response.status === 200) {
              return response.json();
            }
          })
          .then(data => this.setState({ posts: data, loaded: true }));
    }


    render() {
        return (
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
        )
    }
}

export default Posts
