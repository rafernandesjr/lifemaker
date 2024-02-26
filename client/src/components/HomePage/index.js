import React, { useState, useEffect } from 'react';
import { StyledHomePage } from './styles';
import axios from 'axios';

const HomePage = () => {
    // Define o estado para armazenar os personagens
    const [characters, setCharacters] = useState([]);

    // Define um efeito para carregar os personagens ao carregar o componente
    useEffect(() => {
        // Função para carregar os personagens da API
        const fetchCharacters = async () => {
            try {
                // Faz uma solicitação GET para obter os personagens da API
                const response = await axios.get('http://localhost:5000/api/characters');

                // Define o estado dos personagens com os dados recebidos da API
                setCharacters(response.data);
            } catch (error) {
                // Exibe um erro se ocorrer um problema ao carregar os personagens
                console.error('Erro ao buscar personagens:', error);
            }
        };

        // Chama a função para carregar os personagens
        fetchCharacters();
    }, []); // O array vazio indica que este efeito é executado apenas uma vez, ao montar o componente
  
  return (
    <StyledHomePage>
      <h2>Este é o componente HomePage</h2>
      <p>Bem-vindo à página inicial!</p>
      {/* Mapeia os personagens e exibe seus nomes em uma lista */}
      {characters.map(character => (
        <li key={character.id}>{character.name}</li>
    ))}
    </StyledHomePage>
  );
}

export default HomePage;
