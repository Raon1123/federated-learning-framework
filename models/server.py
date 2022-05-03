import torch

class FLServer:

    def __init__ (self):
        # Define clients
        pass

    def update_clients(self):
        """
        Update clients from server.
        """
        pass

    def train_clients(self):
        """
        Train each client locally.
        """
        pass

    def aggregate_clients_info(self):
        """
        Aggregate information from clients.
        """
        pass

    def select_clients(self):
        """
        Actively select clients.
        무엇을 선택할 것인가?
        - random: 랜덤
        - loss: 로스 값
        - sample size: 각 local의 sample 크기
        - similarity based: 유사도를 기준으로.
        - curriculum based: 쉬운 것 -> 쉽고 어려운 것
        """
        pass

    def update_server(self):
        """
        Update server
        """
        pass

    def evaluate_server(self):
        """
        Evaluate server
        """
        pass

    def save_model(self):
        """
        Save results
        """
        pass