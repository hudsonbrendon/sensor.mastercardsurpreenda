![hacs_badge](https://img.shields.io/badge/hacs-custom-orange.svg) [![BuyMeCoffee][buymecoffeebedge]][buymecoffee]

# Matercard Surpreenda Sensor Component

![logo.jpg](logo.png)

Componente customizado para obter informações sobre a pontuação do Mastercard Surpreenda no home assistant.

# Instalação

## HACS

- Tenha o [HACS](https://hacs.xyz/) instalado, isso permitirá que você atualize facilmente.
- Adicione https://github.com/hudsonbrendon/sensor.mastercardsurpreenda como um repositório personalizado do Tipo: Integração
- Clique em Instalar na integração "Mastercard Surpreenda".
- Reinicie Home-Assistant.

## Manual

- Copie o diretório custom_components/mastercard para o seu diretório <config dir>/custom_components.
- Configure.
- Reinicie o Home-Assistant.

# Configuração

```yaml
- platform: mastercard
  email: email
  password: password
```

# Debugando

```yaml
logger:
  default: info
  logs:
    custom_components.mastercard: debug
```

[buymecoffee]: https://www.buymeacoffee.com/hudsonbrendon
[buymecoffeebedge]: https://camo.githubusercontent.com/cd005dca0ef55d7725912ec03a936d3a7c8de5b5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6275792532306d6525323061253230636f666665652d646f6e6174652d79656c6c6f772e737667
