import React from 'react';

class SearchBar extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            thread_code: '',
            group_name:'iqtree',
            start_date:'',
            end_date:'',
            display_number:10,
            response_data:{}

        };
        this.searchByIDURL= 'http://127.0.0.1:5000/search_by_id'
        this.searchByKeywordURL = 'http://127.0.0.1:5000/search_by_keyword'
        this.searchByTagURL = 'http://127.0.0.1:5000/search_by_tag'
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event){
        if(event.target.name==='thread_code'){
            this.setState({thread_code:event.target.value})
        }
        else if(event.target.name==='start_date'){
            this.setState({start_date:event.target.value})
        }
        else if(event.target.name==='end_date'){
            this.setState({end_date:event.target.value})
        }
    }

    handleSubmit(event){
        var prefix = this.state.thread_code.substr(0,1);
        if(prefix==='!'){
            this.setState({thread_code:this.state.thread_code.substr(1)});
        }else if(prefix==='#'){
            this.SearchByTag()
            .then(response=>response.json())
            .then(response=>{
                this.props.setSearchByTagResult(response)
                // console.log(response)
            }).catch(err=>{
                console.log(err);
            });
        }else if(prefix==='$'){
            this.SearchByKeyword()
            .then(response=>response.json())
            .then(response=>{
                this.props.setSearchByKeywordResult(response)
                // console.log(response)
            }).catch(err=>{
                console.log(err);
            });
        }else{
            this.SearchByThreadID()
            .then(response=>response.json())
            .then(response=>{
                this.setState({response_data:response});
                this.props.setPredictTag(this.state.response_data)
            }).catch(err=>{
                console.log(err);
            });
        }
        event.preventDefault();
    }

    SearchByTag(){
        var json_data= JSON.stringify({
            tag:this.state.thread_code.substr(1),
            group_name:this.state.group_name,
            start_date:this.state.start_date,
            end_date:this.state.end_date,
            display_number:this.state.display_number
        })
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: json_data
        };
        return fetch(this.searchByTagURL,requestOptions)
    }

    SearchByKeyword(){
        var json_data= JSON.stringify({
            keyword:this.state.thread_code.substr(1),
            group_name:this.state.group_name,
            start_date:this.state.start_date,
            end_date:this.state.end_date,
            display_number:this.state.display_number
        })
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: json_data
        };
        return fetch(this.searchByKeywordURL,requestOptions)
        
    }


    SearchByThreadID(){
        var json_data= JSON.stringify({
            thread_code:this.state.thread_code,
            group_name:this.state.group_name,
            start_date:this.state.start_date,
            end_date:this.state.end_date,
            display_number:this.state.display_number
        })
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: json_data
        };
        return fetch(this.searchByIDURL,requestOptions)
        
        
    }

    render(){
        return(
            <div className='search_bar'>
                <div >
                    <input className="search_input" type='text' name='thread_code' placeholder='Search ....' onChange={this.handleChange} value={this.state.thread_code}></input>
                    <button className="controls search_btn" name='search_button' onClick={this.handleSubmit} type="submit" >Search</button>
                </div>
                <div>
                    <input className='date_input' type='date' name='start_date' onChange={this.handleChange} value={this.state.start_date}></input>
                    <input className='date_input' type='date' name='end_date' onChange={this.handleChange} value={this.state.end_date}></input>
                </div>
            </div>

        );
    }
}

export default SearchBar;