import React from 'react';

class Document extends React.Component{
    constructor(props){
        super(props);
    }

    render(){
        return (
            <p>{this.props.document.thread_code}</p>
        )
    }
}

class Chart extends React.Component{
    constructor(props){
        super(props);
        
    }

    handleChange(event){

    }

    render(){
        var data = []
        var documents = this.props.documents;
        for(var index=0;index<documents.length;index++){
            console.log(documents[index])
            data.push(<Document key={index} document={documents[index]}/>)
        }
        return(
            <div>
                {data}
            </div>
        );
    }
}

export default Chart;