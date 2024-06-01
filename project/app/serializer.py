from .models import Hudud, QurilishTashkiloti, QuriishBinosi
from rest_framework import serializers

class HududSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Hudud.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)


class QurilishTashkilotiSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    hudud = serializers.CharField(max_length=55)

    def create(self, validated_data):
     return QurilishTashkiloti.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.hudud = validated_data.get('hudud', instance.hudud)


class QurilishBinosiSerializer(serializers.Serializer):
    qurilish_id = serializers.IntegerField()
    hudud_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    maydoni = serializers.CharField(max_length=255)
    qavat = serializers.IntegerField()
    parkovka = serializers.BooleanField(default=True)
    bolalar_maydonchasi = serializers.BooleanField(default=True)
    lift = serializers.BooleanField(default=True)


    def create(self, validated_data):
        return QuriishBinosi.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.qurilish_id = validated_data.get('qurilish_id', instance.qurilish_id)
        instance.hudud_id = validated_data.get('hudud_id', instance.hudud_id)
        instance.name = validated_data.get('name', instance.name)
        instance.maydoni = validated_data.get('maydoni', instance.maydoni)
        instance.qavat = validated_data.get('qavat', instance.qavat)
        instance.parkovka = validated_data.get('parkovka', instance.parkovka)
        instance.bolalar_maydonchasi = validated_data.get('bolalar_maydonchasi', instance.bolalar_maydonchasi)
        instance.lift = validated_data.get('lift', instance.lift)

