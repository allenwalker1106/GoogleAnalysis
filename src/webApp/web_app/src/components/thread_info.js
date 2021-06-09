import React from 'react';


class Tag extends React.Component{
    constructor(props){
        super(props);
        this.state={
            name:'',
            value:this.props.value
        }
    }


    render(){
        return (
            <div>
                {this.state.value}
            </div>
        );
    }
}

class Keyword extends React.Component{
    constructor(props){
        super(props);
        this.state={
            word:this.props.word,
            value:this.props.value
        }
    }


    render(){
        return (
            <div>
                {/* -{this.state.value} */}
                <li>{this.state.word}</li>
            </div>
        );
    }
}

class ThreadInfo extends React.Component{
    constructor(props){
        super(props);
        this.state={
            tag_list:['Reading from folder','Automatic model selection','Substitution model options','Bug report','Rate heterogeneity options','Ascertainment bias correction option','Partition model options','Mixture model options','Heterotachy model options','Site specific frequency model options','Polymorphism aware model options','Automatic partition merging','Tree search parameters','Constrained tree search','Ultrafast bootstrap parameters','Nonparametric bootstrap','Single branch tests','Tree topology tests','Concordance factor','Phylogenetic dating','Ancestral sequence reconstruction','Constructing consensus tree','Propose feature','Likelihood mapping analysis','Utilizing multi core CPUs','Inferring site specific rates','Reducing impact of severe model violations with UFBoot'],
            thread_code:'',
            dict_data:{}
        }
        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event){

    }


    render(){
        var rows=[]
        for(var i=0;i<this.props['tags'].length;i++){
            if(this.props['tags'][i]){
                rows.push(<Tag key={i} value={this.state.tag_list[i]}></Tag>);
            }
        }
        var keywords_props=[]
        for(var key in this.props.keywords_props){
            keywords_props.push(
                <Keyword  key={key} word={key} value={this.props.keywords_props[key]}></Keyword>
            )
        }
        return(
            <div>
                <div>
                    {rows}
                </div>
                <br/>
                <div>
                    <ol>
                        {keywords_props}
                    </ol>
                </div>
            </div>
        )
    }
}

export default ThreadInfo;