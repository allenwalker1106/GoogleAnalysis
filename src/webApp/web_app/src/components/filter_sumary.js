import React from 'react'


function Row(data){
    return(
        <tr>
            <td> </td>
            <td>{data.thread_code}</td>
            <td>{data.init_date}</td>
            <td>{data.last_update}</td>
        </tr>
    )
}

export default class ThreadCodeDisplay extends React.Component{
    constructor(props){
        super(props);
    }


    render(){
        var rows = []
        for(var key in this.props.thread_code){
            rows.push(
                <Row  key={key} thread_code={this.props.thread_code[key]} init_date={this.props.init_date[key]} last_update={this.props.last_update[key]}></Row>
            )
        }
        return (
        <table className='thread_code_table'>
            <tbody>
                <tr>
                    <th>Filter Sumary</th>
                    <th>Thread Code</th>
                    <th>Initilize Date</th>
                    <th>Last update</th>
                </tr>
                {rows}
            </tbody>
        </table>
        );
    }
}