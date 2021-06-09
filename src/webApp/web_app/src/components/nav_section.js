import React from 'react';

class NavSection extends React.Component{
    constructor(props){
        super(props);
    }

    render(){
        return(
            <div className='navSection'>
                <div className='mainLogo'>
                    <p>LOGO</p>
                </div>
                <div className='dashboard'>
                    <p>Dashboard</p>
                </div>
                <div className='divider'>
                    <p>----------</p>
                </div>
                <div className='dataSection'>
                    <div>
                        <p>Statistic</p>
                    </div>
                    <div>
                        <p>Data</p>
                    </div>
                </div>
            </div>
        )
    }
}


export default NavSection