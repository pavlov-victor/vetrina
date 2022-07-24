from rest_framework import serializers

from shops.models import Market, MarketTag, MarketItem


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketTag
        fields = '__all__'


class PublicMarketListSerializer(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Market
        fields = '__all__'


class UserMarketListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        exclude = ['is_verify', 'owner']

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        instance: Market = super(UserMarketListCreateSerializer, self).create(validated_data)
        instance.tags.add(*MarketTag.objects.filter(id__in=tags))
        return instance


class UserMarketDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        exclude = ['is_verify', 'owner']


class MarketItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketItem
        fields = '__all__'


class UserMarketItemListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketItem
        fields = '__all__'


class UserMarketItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketItem
        fields = '__all__'
