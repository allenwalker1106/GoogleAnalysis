import React from 'react'


function Row(data){
    return(
        <tr>
            <td> </td>
            <td>{data.word}</td>
            <td>{data.value}</td>
        </tr>
    )
}

export default class KeywordDisplay extends React.Component{
    constructor(props){
        super(props);
        this.state={
            word:this.props.word,
            value:this.props.value
        }
    }


    render(){
        var rows = []
        for(var key in this.props.keywords_props){
            rows.push(
                <Row  key={key} word={key} value={this.props.keywords_props[key]}></Row>
            )
        }
        return (
        
            <table className='keyword_table'>
                <tbody>
                    <tr>
                        <th>Top ten Keyword</th>
                        <th>Keyword</th>
                        <th>TF-IDF Value</th>
                    </tr>
                    {rows}
                </tbody>
            </table>
        );
    }
}