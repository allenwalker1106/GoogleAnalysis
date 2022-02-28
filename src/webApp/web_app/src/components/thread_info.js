import React from 'react'
import '../static/styles/ThreadInfo.css'

function Comment(data){
    return (

        <div className="comment-content">
            {data.value}
        </div>
    )
}

export default class ThreadDisplay extends React.Component{
    constructor(props){
        super(props);
        this.state={
            thread_data:[],
            topic:[]
        }
    }

    render(){
        var thread_data = this.state.thread_data
        var comments= []
        var topic = []
        if(this.props.dict_data){
            topic.push(
                <div className='thread_header'>
                    <p>Topic:</p>
                </div>
            )
            topic.push(<Comment className='topic' value={'Topic: '+this.props.dict_data.topic}></Comment>)
            // console.log(this.props.dict_data.topic)
            topic.push(
                <div className='thread_header'>
                    <p>Content:</p>
                </div>
            )
            for(var comment in this.props.dict_data.content){
                comments.push(<Comment key={comment} value={this.props.dict_data.content[comment]}></Comment>)
            }
        }
        return(
            <div className="comments-container">
                        {topic}
                        {comments}
                        {/* <ul className="comments-list reply-list">
                            {comments}
                        </ul>  */}
            </div>      
        );
    }
}