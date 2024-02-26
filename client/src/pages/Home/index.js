import React from 'react';
import HomePage from '../../components/HomePage'; // Importando o componente HomePage
import styled from 'styled-components';

const StyledHome = styled.div`
  /* Estilos específicos da página Home */
`;

const Home = () => {
  return (
    <StyledHome>
      <HomePage /> {/* Renderizando o componente HomePage */}
    </StyledHome>
  );
}

export default Home;
