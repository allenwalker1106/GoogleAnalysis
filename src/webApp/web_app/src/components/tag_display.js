import React from 'react'


function Tag(data){
    return(
        <div className="tag">
            <label>{data.value}</label>
        </div>
    )
}


export default class TagDisplay extends React.Component{
    constructor(props){
        super(props);
        this.state={
            tag_list:['Reading from folder','Automatic model selection','Substitution model options','Bug report','Rate heterogeneity options','Ascertainment bias correction option','Partition model options','Mixture model options','Heterotachy model options','Site specific frequency model options','Polymorphism aware model options','Automatic partition merging','Tree search parameters','Constrained tree search','Ultrafast bootstrap parameters','Nonparametric bootstrap','Single branch tests','Tree topology tests','Concordance factor','Phylogenetic dating','Ancestral sequence reconstruction','Constructing consensus tree','Propose feature','Likelihood mapping analysis','Utilizing multi core CPUs','Inferring site specific rates','Reducing impact of severe model violations with UFBoot'],
            thread_code:'',
            dict_data:{}
        }
    }
    
    render(){
        var rows=[]
        for(var i=0;i<this.props['tags'].length;i++){
            if(this.props['tags'][i]){
                rows.push(<Tag key={i} value={this.state.tag_list[i]}></Tag>);
            }
        }
        return(
            
            <div className="tag-wrapper">
                <p>Predicted Label</p>
                <hr className="dotted"></hr>
                {rows}
            </div>
        );
    }
}